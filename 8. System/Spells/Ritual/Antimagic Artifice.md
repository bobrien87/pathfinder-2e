---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "9"
cast: "1 day"
range: "touch"
targets: "one inanimate object of 1 Bulk or less"
duration: "1 week (see text)"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You anoint a seemingly harmless item with the power to disrupt magic. As part of performing this ritual, you set a trigger for when the target object activates. The object remains enchanted for 1 week or until it's activated, whichever comes first.

For 10 minutes after the object is activated, magic is suppressed within an emanation centered on the object. Spells can't penetrate the area, magic items cease to function within it, and no one inside can cast spells or use magic abilities. Likewise, spells—such as dispel magic—can't affect the emanation unless they're of a higher rank than the ritual. Magic effects resume the moment they pass outside the emanation. For example, a caster outside of the emanation could target a fireball on a spot on the other side of the emanation, even if the line of effect passes through the emanation. A summoned creature winks out of existence if it enters the emanation but reappears if the emanation ends. Invested magic items cease to function, but they remain invested and resume functioning when they exit the emanation; the attribute boost from an apex item isn't suppressed within the field. Spells of a higher rank than antimagic artifice overcome its effects and can even be cast by a creature within the field.

The emanation disrupts only magic, so a +3 longsword still functions as a longsword. Magically created creatures (such as constructs with the magical trait) function normally within the emanation.
- **Critical Success** When triggered, the antimagic emanation has a radius of 100 feet. The ritual casters are unaffected by the emanation.
- **Success** When triggered, the antimagic emanation has a radius of 50 feet.
- **Failure** The ritual has no effect.
- **Critical Failure** The magic of the ritual backfires, scrambling the casters' minds. Each caster is [[Stupefied 4]]. The value of this condition is reduced by 1 for each day that passes, and it can't be removed or reduced by any other means.

**Source:** `= this.source` (`= this.source-type`)
