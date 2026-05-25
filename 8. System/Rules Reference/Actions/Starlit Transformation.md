---
type: action
source-type: "Remaster"
traits: ["[[Arcane]]"]
cast: "`pf2:1`"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per hour

**Effect** Light swirls around you, transforming your armor, clothing, and a single weapon in your possession into a specific alternate outfit. While your equipment might look dramatically different, it functions as normal. If someone attempts to discern your identity, they must use a [[Seek]] action to attempt a Perception check against your Deception DC, as if you were using the [[Impersonate]] action. Your Deception DC against such attempts is 20 + your proficiency modifier instead of the normal DC. Unlike with Impersonate, you don't have to attempt a Deception check to interact with someone to conceal your identity—a check happens only if someone else specifically tries to uncover it. You remain in your sentinel form for 10 minutes or until you use Starlit Transformation again to change back to your normal form.

While you're in sentinel form, your transformed weapon shines with starlight and gains a +1 status bonus to damage rolls with the weapon. You can fling bolts of starlight from your weapon with a Strike action, using your melee attack modifier with the weapon. These bolts deal 1d4 force damage, have a range of 60 feet, are affected by your weapon runes, and have the arcane and force traits.

**Source:** `= this.source` (`= this.source-type`)
