---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Cursebound]]", "[[Divine]]", "[[Fire]]", "[[Oracle]]"]
prerequisites: "cosmos or flames mystery"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your lips murmur as you portend a great disaster, one you hope you survive. A rain of blazing bolts begins to fall from the heavens in a @Template[emanation|distance:10], centered on you, that deals @Damage[2d6[fire]|options:area-damage] damage to all creatures in the emanation at the end of each of your turns ([[Reflex]] save); you can't exclude yourself from the emanation. The skyfire persists for 1 minute; while you can't Dismiss it, you can suppress the effect for 1 round with a Sustain action. The rain of fire is suppressed if you fall [[Unconscious]]. If you become [[Cursebound 3]] or 4 at any point during Trial by Skyfire's duration, the emanation increases to @Template[emanation|distance:15]{15 feet} and the damage increases to @Damage[4d6[fire]|options:area-damage|shortLabel].

**Source:** `= this.source` (`= this.source-type`)
