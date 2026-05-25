---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]", "[[Healing]]"]
price: "{'gp': 300}"
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

Contagion metabolizers seek out toxins in the bloodstream and attempt to purify them into humors the body processes naturally. When you drink this elixir, it attempts a counteract check with a +19 modifier to remove the highest-level poison or disease afflicting you. The elixir has a counteract rank of 6. This takes longer for a disease—the counteract check doesn't happen until 10 minutes after you drink the elixir. After drinking, you become temporarily immune to contagion metabolizers for 1 hour.

If you're a chirurgeon alchemist and have powerful alchemy, you can substitute your statistics when you create a contagion metabolizer using Quick Alchemy, if your stats are higher. This replaces the counteract rank with half your level rounded up and the counteract modifier with your class DC – 10.

**Source:** `= this.source` (`= this.source-type`)
