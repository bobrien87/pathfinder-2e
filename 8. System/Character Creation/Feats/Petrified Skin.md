---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Aftermath]]", "[[Magical]]"]
prerequisites: "You have been petrified by an enemy"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

It might have been a medusa, basilisk, or even a paleohemoth; regardless of the source, you were the target of some petrifying effect, and an element of that stony gaze has remained with you, both protecting and slowly consuming you. Your limbs are coated with a layer of stone that rests atop your skin and covers more of your body as you lose health. You gain a stone fist unarmed attack that deals 1d8 bludgeoning damage, has the shove trait, and is in the brawling weapon group (unlike a normal fist, it doesn't have the agile or finesse traits).

Additionally, you become more petrified as your life force ebbs. When you have fewer than half your maximum Hit Points, you increase the damage die size of your stone fist from 1d8 to 1d10 and gain resistance to physical damage (except adamantine) equal to your Constitution modifier.

If you would gain the dying condition, you can choose to instead be permanently petrified and avoid the risk of death. When you do, you enter your petrified form with your full maximum Hit Points instead of the normal number. If you become unpetrified, you return to 0 Hit Points, as normal. You can't voluntarily end this petrification. An effect that suppresses, counteracts, or otherwise ends petrification (such as sure footing) functions against this petrification, but has no effect against the petrification unless the effect has a counteract rank equal to half your level or higher and the effect's creator succeeds at a counteract check against the hard DC for your level. Each time you recover from this petrification, you gain a new scar on your skin in the shape of a long, thin crack.

**Source:** `= this.source` (`= this.source-type`)
