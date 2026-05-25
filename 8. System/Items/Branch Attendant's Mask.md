---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 25}"
usage: "worn"
bulk: "—"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Although not all attendants' masks are enchanted, many apply a first enchantment to celebrate their acceptance into a branch of the academy. While you wear the mask or have it as your bonded item, add the associated cantrip to your prepared cantrips. This has no effect if you do not prepare cantrips from the arcane or primal lists.

- **Cascade Bearers** [[Read Aura]]
- **Emerald Boughs** [[Root Reading]]
- **Rain-Scribes** [[Deep Breath]]
- **Tempest-Sun Mages** [[Electric Arc]]
- **Uzunjati**

**Source:** `= this.source` (`= this.source-type`)
