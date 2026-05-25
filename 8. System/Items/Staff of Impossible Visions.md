---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Magical]]", "[[Staff]]", "[[Two hand d8]]"]
price: "{'gp': 230}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This bizarre staff is made from oak, capped with a cluster of eye-shaped gemstones that seem to move and undulate at the corner of your vision. While wielding the staff, you can peer through the eyes on the staff rather than your own, using your normal visual senses (including any benefits of spells like [[See the Unseen]]). You can maneuver the staff to see things around corners, at higher elevations, or in places where the staff can fit but your head can't. This doesn't provide sufficient line of effect to target creatures around corners. The eyes are as vulnerable as your eyes and can be affected by anything that alters your vision, such as a blinding flash of light.

**Activate** Cast a Spell

**Effect** You expend a number of charges from the staff to cast a spell from its list.

- **Cantrip** [[Daze]]
- **1st** [[Fear]], [[Phantom Pain]]
- **2nd** [[Augury]], [[Paranoia]]

**Craft Requirements** Supply one casting of all listed ranks of all listed spells.

**Source:** `= this.source` (`= this.source-type`)
