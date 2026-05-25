---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 550}"
usage: "wornmask"
bulk: "—"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This soft covering for the mouth and nose is made from the sleek fur of a dweomercat and is fastened with two gnarled teeth of the same beast. Each day during daily preparations, you must brush and oil the veil. At the conclusion of the activity, select one tradition of magic (arcane, divine, occult, or primal). You gain a +1 item bonus to all saves against magic from that tradition until your next daily preparations.

**Activate—Dimension Leap** R (concentration, teleportation)

**Frequency** once per day

**Trigger** You succeed at a saving throw against a spell from the chosen tradition

**Effect** Your veil billows out and you disappear behind it. You use the traces of dweomercat magic to teleport yourself instantly to any unoccupied square within 30 feet. If you critically succeeded at the triggering save, you can instead teleport within 45 feet.

**Craft Requirements** The initial raw materials must include the hide and teeth of a dweomercat.

**Source:** `= this.source` (`= this.source-type`)
