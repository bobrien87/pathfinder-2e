---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]"]
price: "{'gp': 1}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

This clear, bitter liquid can be ingested to change certain secondary sex characteristics. Different formulations create different changes—for example, one variety might cause the voice to deepen and promote body and facial hair growth, while another might cause fat redistribution around the hips and the growth of breasts. These changes tend to be accompanied by shifting of the fat in the face, sometimes dramatically or sometimes more subtly changing the user's appearance.

The elixir must be taken every week, and changes occur over the course of a year or more.

**Source:** `= this.source` (`= this.source-type`)
