---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Consumable]]", "[[Magical]]", "[[Mental]]", "[[Potion]]"]
price: "{'gp': 65}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

The pale liquid of *empath's cordial* changes color to reflect the mood of the creature nearest to it—turning blue for calm, red for anger, and green for envious, among other hues. For 1 hour after you drink this potion, you can sense the presence of general emotions, such as hostility toward you or the presence of an emotion effect impacting a creature's emotions, within 30 feet. A creature that failed a saving throw against [[Calm]] can't be detected. This potion doesn't allow you to automatically tell what emotions a specific creature is experiencing, but you can attempt a Perception check with a +2 item bonus (DC set by the GM) to discern that information. The potion also grants you a +1 item bonus to Perception checks to [[Sense Motive]] against creatures whose emotions you can sense.

**Source:** `= this.source` (`= this.source-type`)
