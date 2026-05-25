---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Alchemical]]"]
price: "{'gp': 133}"
usage: "worncollar"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This intimidating collar contains a hollow central tube and ends in twin metal points shaped like spider fangs. The collar can be loaded with an alchemical mutagen as an Interact action.

**Activate** `pf2:f` (manipulate)

**Trigger** You roll initiative

**Requirements** A mutagen is loaded in the collar

**Effect** The metal points dig into your neck, inflicting 1 piercing damage and injecting the mutagen directly into your bloodstream. This has the same effect as if you drank the mutagen conventionally, except the duration of the mutagen is halved due to the more direct administration.

**Source:** `= this.source` (`= this.source-type`)
