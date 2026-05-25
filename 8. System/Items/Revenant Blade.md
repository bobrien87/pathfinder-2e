---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Agile]]", "[[Finesse]]", "[[Invested]]", "[[Magical]]", "[[Trip]]", "[[Void]]"]
price: "{'gp': 900}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The mortal agents of powerful necromancers are a varied lot, but they tend to share two things in common: a deep and abiding fear of death, and a desperate hope that loyalty to their foul masters might be rewarded with some means of transcending it. To most of these wretched souls, this simple *+1 striking sickle* is as close as they will ever come to realizing that desire.

Revenant blades are usually created in large numbers to arm a necromancer's mortal troops before sending them into battle, and despite their name, they can be crafted from whichever base weapon is best suited for the expected conflict. Whatever form it takes, every revenant blade is adorned in some way with a small gem of deep black onyx. When you invest in the weapon, a small portion of your soul is transferred into the gem, bonding it to you and granting the weapon the effects of the Decaying rune for as long as it remains invested.

Should you die in battle while invested in a revenant blade, its gem shatters, and your corpse rises 1 round later to continue the fight. You become an undead creature under the GM's control, although you generally retain the motivations and loyalties you had in life. The GM chooses what type of undead you become, selecting an appropriate undead creature that has a level no greater than your level – 5, to a minimum of 0. You can't be raised from the dead by any means short of a wish ritual until your undead form is destroyed.

**Source:** `= this.source` (`= this.source-type`)
