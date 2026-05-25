---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Invested]]", "[[Magical]]", "[[Tattoo]]"]
price: "{'gp': 10}"
usage: "tattooed-on-the-body"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Common among fatalists and adventurers with access to resurrection magic, mortal chronicles look like tombstones, funeral plaques, or simple scrolls bearing the wearer's name or nickname. If you die, the date and cause of your death appear on the tattoo. The cause is literal and inexact, failing to identify specifics; it could read "beheaded" or "immolated" but not "beheaded by Amiri" or "murdered with fire." If you're raised from the dead, a mark on the tattoo indicates the date you reversed your death. The tattoo then expands enough to list your next death when it comes.

**Source:** `= this.source` (`= this.source-type`)
