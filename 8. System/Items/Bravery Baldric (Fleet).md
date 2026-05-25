---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 150}"
usage: "worn"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *bravery baldric* is a belt that wraps around the shoulder and draws on your well of courage. When you critically succeed on a save against a fear effect or reduce your frightened condition to 0, the baldric gains 1 charge, which slightly alters the color, turning it grass green. A *bravery baldric* can hold up to 2 charges, and its charges reset to 0 when you invest it. You can have only one *bravery baldric* invested at a time.

**Activate** `pf2:2` (concentrate)

**Frequency** once per hour; **Cost** 1 charge from the baldric

**Effect** The baldric is grass green when charged, and it casts [[Fleet Step]] on you.

**Source:** `= this.source` (`= this.source-type`)
