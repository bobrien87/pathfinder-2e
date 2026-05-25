---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]", "[[Healing]]"]
price: "{'gp': 9}"
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

This elixir bolsters your body's natural defenses and ability to resist maladies that travel through or affect blood. For 10 minutes you receive resistance 5 to persistent bleed and persistent poison damage, and you lower the DC for any flat checks to end persistent bleed or persistent poison damage as if you received particularly appropriate aid.

At the GM's discretion, blood booster elixirs can also automatically counteract non-magical effects that specifically rely on thinning the drinker's blood, such as a skull peeler's anticoagulant.

> [!danger] Effect: Blood Booster

**Source:** `= this.source` (`= this.source-type`)
