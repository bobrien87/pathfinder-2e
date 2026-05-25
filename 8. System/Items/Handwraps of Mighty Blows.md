---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 35}"
usage: "worngloves"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

As you invest these embroidered strips of cloth, you must meditate and slowly wrap them around your hands. These handwraps have weapon runes etched into them to give your unarmed attacks the benefits of those runes, making your unarmed attacks work like magic weapons. For example, *+1 striking handwraps of mighty blows* would give you a +1 item bonus to attack rolls with your unarmed attacks and increase the damage of your unarmed attacks from one weapon die to two (normally 2d4 instead of 1d4, but if your fists have a different weapon damage die or you have other unarmed attacks, use two of that die size instead).

You can upgrade, add, and transfer runes to and from the handwraps just as you would for a weapon, and you can attach talismans to the handwraps. Treat the handwraps as melee weapons of the brawling group with light Bulk for these purposes. Property runes apply only when they would be applicable to the unarmed attack you're using. For example, a property that must be applied to a slashing weapon wouldn't function when you attacked with a fist, but you would gain its benefits if you attacked with a claw or some other slashing unarmed attack.

**Source:** `= this.source` (`= this.source-type`)
