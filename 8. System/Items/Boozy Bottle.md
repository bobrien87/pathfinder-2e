---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Invested]]", "[[Magical]]", "[[Tattoo]]"]
price: "{'gp': 140}"
usage: "tattooed-on-the-body"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This tattoo depicts a container of alcohol, traditionally a small, uncorked brown bottle. You gain a +1 item bonus to saving throws against poison.

**Activate** R (concentrate)

**Frequency** once per day

**Trigger** You fail (but don't critically fail) an initial saving throw against a poison, or you gain persistent poison damage

**Effect** You pick your poison. Calling out the name of a drink as though ordering at a bar, you negate the triggering poison. Instead, you become slightly drunk. For 10 minutes you're [[Off Guard]] and gain a +1 item bonus to saving throws against fear.

> [!danger] Effect: Boozy Bottle

**Source:** `= this.source` (`= this.source-type`)
