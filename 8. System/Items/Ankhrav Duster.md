---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Agile]]", "[[Free hand]]", "[[Magical]]", "[[Monk]]"]
price: "{'gp': 90}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Acid drips from the ankhrav mandibles protruding from this *+1 [[Knuckle Duster]]*. Strikes with this weapon deal an additional 1 acid damage.

**Activate—Caustic Jabs** `pf2:1` (concentrate)

**Frequency** once per hour

**Effect** Until the end of your next turn, your Strikes with the *ankhrav duster* deal an additional 1d6 persistent acid damage.

> [!danger] Effect: Caustic Jabs

**Craft Requirements** The initial raw materials must include the mandibles of an ankhrav.

**Source:** `= this.source` (`= this.source-type`)
