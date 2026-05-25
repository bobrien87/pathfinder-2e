---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Invested]]", "[[Magical]]", "[[Tattoo]]"]
price: "{'gp': 220}"
usage: "tattooed-on-the-body"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

While dormant, this tattoo appears to be a simple flower bud, but when activated the flower swiftly blossoms, remaining that way until the next time you make your daily preparations. These blooms are colorful, elegant representations of magnolia flowers.

**Activate** `pf2:2` envision

**Frequency** once per day

**Effect** Choose a willing ally you can see within 30 feet. Your ally seems more charming, though no one can pinpoint why. They gain a +1 status bonus to Diplomacy checks for 10 minutes. Once on their next turn, the ally can attempt to draw a creature's attention. To do so, the ally must spend 1 action (which has the emotion, mental, and visual traits) to select a creature the ally can see and make eye contact in a way the target can see. The target must succeed at a DC 20 [[Will]] save or be [[Fascinated]] with your ally until the end of that ally's next turn. If the save succeeds or the effect ends, the target is temporarily immune to being fascinated by any *magnolia bewitching bloom* for 24 hours.

> [!danger] Effect: Bewitching Bloom (Magnolia)

**Source:** `= this.source` (`= this.source-type`)
