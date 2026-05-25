---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Illusion]]", "[[Manipulate]]", "[[Mythic]]", "[[Visual]]"]
cast: "`pf2:2`"
duration: "24 hours"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You conjure four magic feathers, each with the potential to hold a single illusory guise. These feathers have negligible Bulk and remain potent for the duration. As an Interact action, you can place one of these feathers into your hair or cap, or remove an already donned feather. When worn in this way, the feather causes you to appear as another creature of the same body shape, and with roughly similar height (within 6 inches) and weight (within 50 pounds), as yourself. The disguise is typically good enough to hide your identity but not to impersonate a specific individual. This disguise also changes your voice and scent, but it doesn't disguise your mannerisms or behavior. You can change the appearance of your clothing and worn items, such as making your armor look like a dress. Held items are unaffected, and any worn item you remove returns to its true appearance.

When you don a feather for the first time, you determine the illusory appearance that feather grants you, selecting the ancestry, age, gender, attire, and other visual features. For the duration, this feather is linked to that disguise. Wearing it in your hair or hat always imparts the linked appearance. Selecting a feather's appearance for the first time counts as setting up a disguise for the [[Impersonate]] use of Deception; attempt this Deception check at mythic proficiency.

You can only wear one feather at a time. When you remove a feather, you revert to your true appearance. If you give a feather to another creature, it can no longer impart a disguise.

**Source:** `= this.source` (`= this.source-type`)
