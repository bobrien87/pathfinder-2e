---
type: item
source-type: "Remaster"
level: "19"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]"]
price: "{'gp': 5200}"
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

Made from several oils of differing hues extracted from jellyfish and rare plants, the layers of chromatic jellyfish oil stack to form a rainbow within their vial. For 10 minutes after consuming chromatic jellyfish oil, you gain resistance 15 to precision damage and extra damage from critical hits. While the effect lasts, you ignore difficult terrain caused by moving through tight spaces that aren't tight enough to force you to [[Squeeze]], and you can move 5 feet per round when you successfully Squeeze (or 10 feet per round on a critical success). You can also [[Crawl]] at half your Speed.

> [!danger] Effect: Chromatic Jellyfish Oil

**Source:** `= this.source` (`= this.source-type`)
