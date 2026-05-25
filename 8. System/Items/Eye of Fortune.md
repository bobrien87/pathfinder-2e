---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 2700}"
usage: "worneyepiece"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Adherents of Erastil, god of the hunt, create these magical eye patches. An *eye of fortune* has a jeweled eye symbol on its front, allowing you to magically see through the eye patch as though it were transparent.

**Activate—Luck Beyond Sight** `pf2:f` (concentrate, fortune)

**Trigger** You attack a concealed or hidden creature and haven't attempted the flat check yet

**Effect** You can roll the flat check for the concealed or hidden condition twice and use the higher result.

**Source:** `= this.source` (`= this.source-type`)
