---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Consumable]]", "[[Fulu]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 70}"
usage: "affixed-to-armor"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:f` (concentrate)

**Trigger** You attempt to [[Escape]].

The *escape fulu* is a charm common among wealthy people, who wear the talisman in case of kidnapping. When you Activate this fulu, for 1 minute, you gain a +2 status bonus to your attempts to Escape as well as to Stealth checks to [[Hide]] and [[Sneak]].

> [!danger] Effect: Escape Fulu

**Source:** `= this.source` (`= this.source-type`)
