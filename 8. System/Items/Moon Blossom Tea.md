---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Consumable]]", "[[Magical]]", "[[Potion]]", "[[Tea]]"]
price: "{'gp': 150}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

This bright and citrusy tea is traditionally made with green tea combined with orange rind shavings and flower petals plucked during a full moon. Some claim to be able to tell the difference if these petals were plucked at other times, but this does not alter the tea's effects. The tea leaves have a chance to anticipate unexpected encounters. After consuming the tea, you gain a +2 item bonus to all initiative rolls for 1 hour and gain the following reaction.

> [!danger] Effect: Moon Blossom Tea

**Evade Peril** R (concentrate, fortune)

**Trigger** You roll a failure on a Reflex save

**Effect** You get a success on the Reflex save instead. Reduce the remaining duration of moon blossom tea by 1 hour; if this reduces the duration to 0, the duration ends.

**Activate—Tea Ceremony** 10 minutes (concentrate, manipulate) The duration increases to 4 hours.

**Source:** `= this.source` (`= this.source-type`)
