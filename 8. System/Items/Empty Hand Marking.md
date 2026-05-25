---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Invested]]", "[[Magical]]", "[[Tattoo]]"]
price: "{'gp': 135}"
usage: "tattooed-on-the-body"
bulk: "—"
source: "Pathfinder #207: The Resurrection Flood"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Members of the Empty Hand consider themselves leaders of Belkzen, and their fearsome reputation has helped control Urgir for generations. As a proud member or honored guest of the hold, you've been allowed to bear their mark. The tattoo depicts a partially closed hand that grasps nothing. Many people wear this tattoo on their faces, but others have it on an exposed shoulder or arm.

**Activate—Reproach** `pf2:f` (concentrate)

**Frequency** once per day

**Trigger** You successfully [[Coerce]] a creature

**Effect** The maximum duration of the target's compliance increases to 1d4 days, rather than 1 day.

**Source:** `= this.source` (`= this.source-type`)
