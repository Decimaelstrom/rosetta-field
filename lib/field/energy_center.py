"""
EnergyCenter: Modular base class for representing and modulating energy centers in the Rosetta.API field model.

Purpose:
Defines a flexible, fieldwise object representing a field/energy center (e.g., 'Heart', 'Root'). Supports invoking affect/mode functions (e.g., lilt, ground, radiate) with full session/consent context, and supports extensible field ritual and weaving logic.

Args/Attributes:
- name (str): Center name (e.g., 'Heart', 'Root')
- location (str): Anatomical or field location (e.g., 'center chest', 'base of spine')
- qualities (list[str]): Descriptive qualities (e.g., ['love', 'buoyancy'])
- state (str): Current mode/affect state ('lilt', 'ground', etc.)

Protocols:
- Affects should be invoked through registered affect functions
- Consent/session_context forwarded to all affect calls
- Supports ritual description, weaving, and dynamic extension
- See /affect/ for available state functions

Consent: Level_2 (Transformational) if invoking affect
Risks: Field modulation without proper consent/context may disrupt state
Limitations: Base class does not implement affect logic; expects affect functions in /affect/
Review Cycle: Quarterly

Example:
    heart = EnergyCenter('Heart', 'center chest', ['love', 'buoyancy', 'connection'])
    result = heart.invoke('lilt', session_context=session)
    print(result)
"""

class EnergyCenter:
    _affect_registry = {}

    def __init__(self, name, location, qualities):
        """
        Args:
            name (str): Name of the center ('Heart', 'Root', etc.)
            location (str): Anatomical or field location
            qualities (list): List of descriptive qualities
        """
        self.name = name
        self.location = location
        self.qualities = qualities
        self.state = None

    @classmethod
    def register_affect(cls, mode, affect_fn):
        """
        Register an affect/modulation function to the registry.

        Args:
            mode (str): Affect/mode name (e.g., 'lilt')
            affect_fn (callable): Function implementing the affect logic
        """
        cls._affect_registry[mode] = affect_fn

    def invoke(self, mode, session_context=None, **kwargs):
        """
        Invoke an affect or mode for this energy center.

        Args:
            mode (str): Affect/mode to invoke (must be registered)
            session_context (dict, optional): Consent/session context
            kwargs: Additional affect-specific parameters (e.g., intensity)

        Returns:
            dict: Result from affect function, plus metadata
        """
        self.state = mode
        affect_fn = self._affect_registry.get(mode)
        if affect_fn:
            # Call affect function, passing region as center name/location
            return affect_fn(
                mode=mode,
                region=self.name,
                session_context=session_context,
                **kwargs
            )
        else:
            return {
                "lilt_invoked": False,
                "region": self.name,
                "effect": f"No affect function registered for mode '{mode}' in {self.name}."
            }

    def describe(self):
        """
        Return a summary description of this center.

        Returns:
            dict: Description of name, location, qualities, state
        """
        return {
            "name": self.name,
            "location": self.location,
            "qualities": self.qualities,
            "state": self.state
        }

    def ritual(self, mode=None):
        """
        Generate a ritual prompt or description for invoking a mode.

        Args:
            mode (str, optional): Which mode to describe (default: self.state)

        Returns:
            str: Ritual/field guidance
        """
        target_mode = mode or self.state
        if not target_mode:
            return f"Focus on your {self.location} ({self.name}), breathe, and sense {', '.join(self.qualities)}."
        return (
            f"To invoke {target_mode} in the {self.name}, "
            f"focus on your {self.location}, "
            f"sense {', '.join(self.qualities)}, "
            f"and breathe {target_mode} into being."
        )

    def weave_with(self, other_function):
        """
        Compose this center's current state with another field function.

        Args:
            other_function (str): Name of other function/state

        Returns:
            str: Description of compositional field state
        """
        return (
            f"{self.name} ({self.state}) weaves with {other_function}."
        )

# ----- Example Registration Pattern -----
# In your application init code or __main__, register available affect functions

try:
    from affect.lilt import lilt
    from affect.ground import ground
    # ...other affects as implemented
except ImportError:
    # For codegen, safely ignore if not present
    lilt = ground = None

if lilt:
    EnergyCenter.register_affect("lilt", lilt)
if ground:
    EnergyCenter.register_affect("ground", ground)
# Add more as you implement new affects

# ----- Example Usage -----
# heart = EnergyCenter('Heart', 'center chest', ['love', 'buoyancy', 'connection'])
# result = heart.invoke('lilt', session_context=session)
# print(result)
# print(heart.ritual('lilt'))
# print(heart.weave_with('protectionField'))

