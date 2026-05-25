---
type: item
source-type: "Remaster"
level: "16"
traits: ["[[Invested]]", "[[Magical]]", "[[Mythic]]"]
price: "{'gp': 10000}"
usage: "worn"
bulk: "—"
source: "Pathfinder #220: Crypt of Runes"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The mightiest wizards of Eurythnia, the realm of lust, would sometimes share one of these pairs of bracelets—the silver, most often—with their closest confidantes and most trusted apprentices, while keeping the golden one for themselves.

**Activate—Grant Mythic Power** 1 minute (concentrate)

**Requirements** Both bracelets are invested and the silver bracelet is not already imbued with mythic power

**Effect** The wearer of the golden bracelet imbues the silver bracelet with a portion of their mythic power by spending 1 Mythic Point. Until the silver bracelet is no longer imbued with mythic power, the maximum number of Mythic Points the wearer of the golden bracelet can have is reduced by 1. Whenever the wearer of the silver bracelet would attempt a skill check, they can choose to make the check at mythic proficiency. If they do, the silver bracelet loses its mythic power and the wearer of the golden bracelet is immediately aware of this, regardless of the distance between the two bracelets, even if they are on different planes of existence. If the creature who had invested in the silver bracelet dies before expending the mythic power in it, the silver bracelet immediately teleports into the possession of the wearer of the golden bracelet regardless of the distance between them, even if they are on different planes of existence.

**Source:** `= this.source` (`= this.source-type`)
