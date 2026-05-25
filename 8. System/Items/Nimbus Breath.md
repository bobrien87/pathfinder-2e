---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Air]]", "[[Bottled breath]]", "[[Consumable]]", "[[Electricity]]"]
price: "{'gp': 80}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

The dwarves of Cloudspire Citadel in Golarion's Mwangi Expanse create bottles of *nimbus breath* by capturing and bottling the fluffiest nimbus clouds from the lairs of cloud dragons. After harvesting the cloud, the bottle must sit at the peak of the tallest mountain for 10 days and 10 nights, pelted by all forms of weather. *Nimbus breaths* can also be created by capturing clouds on other planes, such as those found on the Plane of Air or in the highest peaks of Celestia.

After you inhale the *nimbus breath*, you gain resistance 5 to electricity and are affected by [[Fly]] as long as you hold your breath.

You can exhale the breath as a single action to create a [[Gust of Wind]] (DC 24) from your mouth. If you're airborne when the cloud expires, you float gently to the ground at 60 feet per round and don't take damage from this fall.

> [!danger] Effect: Nimbus Breath

**Source:** `= this.source` (`= this.source-type`)
