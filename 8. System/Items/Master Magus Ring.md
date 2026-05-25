---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Arcane]]", "[[Focused]]", "[[Invested]]"]
price: "{'gp': 1250}"
usage: "worn"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Elegant jewelry such as the *master magus ring* adorns experienced magi. Each ring has a significant metal and symbol to represent a particular hybrid study, such as a heavy iron ring with an icon of a mountain for [[Inexorable Iron]], or glittering silver with a shield-like emblem for [[Sparkling Targe]]. You gain a +2 item bonus to Arcana checks.

**Activate** `pf2:f` (concentrate)

**Frequency** once per day

**Effect** You gain 1 Focus Point, which you can use only to cast a magus conflux spell. If not used by the end of your turn, this Focus Point is lost.

**Activate** `pf2:f` (concentrate)

**Frequency** once per day

**Effect** The ring transports you and any items you're wearing and holding from your current space to an unoccupied space you can see within a range equal to your Speed. If this would bring another creature with you—even if you're carrying it in an extradimensional container—the activation fails and is used.

**Craft Requirements** You are a magus.

**Source:** `= this.source` (`= this.source-type`)
