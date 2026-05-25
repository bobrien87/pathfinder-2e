---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Air]]", "[[Magical]]"]
price: "{'gp': 130}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This object can only be described as a gray, solidified, miniature cloud that feels spongy to the touch. The cloud is incredibly soft and can be easily lifted with little effort, though its ephemeral nature requires using two hands to ensure it doesn't slip from your grasp.

**Activate** `pf2:1` (manipulate)

**Frequency** once per day

**Effect** You blow across the surface of the cloud, and it floats free of you and calls up a strong breeze. For the next 8 hours, it floats behind you and your companions, increasing the amount of time the group can Hustle during exploration to the lowest Constitution modifier in the group × 20 instead of × 10. You must all remain within 100 feet to get the benefit. If you activate the item aboard a vehicle, you instead grant the vehicle a +10-foot circumstance bonus to its Speeds for 8 hours. If the vehicle is powered by wind, such as a sailing ship, the bonus increases to +20 feet. When the 8 hours are up, the cloud stops blowing and floats back into your hands.

**Source:** `= this.source` (`= this.source-type`)
