---
type: item
source-type: "Remaster"
level: "5"
price: "{'gp': 80}"
usage: "worngarment"
bulk: "2"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Monster suits are used in elaborate and often tawdry performances where actors portray monstrous creatures. These shows tend to feature gratuitous special effects and culminate with the costumed actors engaging in mock battles on stage, to audiences' delight.

A monster suit is crafted to resemble a specific creature with the animal, beast, dragon, fiend, giant, plant, or undead trait. You can wear a monster suit that resembles a creature that is your size or one size larger, though this doesn't change your actual size. It takes 10 minutes to don a monster suit, and when wearing one, you take a –10-foot item penalty to your Speeds and a –4 circumstance penalty to skill checks for move actions due to the suit's unwieldy shape. However, the monster suit counts as a using a disguise kit for [[Impersonating]] the associated creature, and you gain a +2 item bonus to your Deception check and DC for the activity.

**Source:** `= this.source` (`= this.source-type`)
