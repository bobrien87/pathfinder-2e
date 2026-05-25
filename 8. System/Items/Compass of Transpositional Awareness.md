---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Invested]]", "[[Magical]]", "[[Teleportation]]"]
price: "{'gp': 950}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The silver face of this glass-encased compass is etched with dozens of esoteric symbols, obscure icons, and inscrutable abbreviations.

**Activate—Track Teleportation** `pf2:1` (concentrate, manipulate)

**Frequency** once per minute

**Effect** You point the compass of transpositional awareness at an extant teleportation effect (such as a magical portal) or the site of a teleportation effect that existed within the last 1 minute (such as the space where a creature just cast [[Translocate]]). Attempt an Occultism check to determine to where the effect leads or led. The DC of this check is the effect's counteract DC. On a success, you know roughly the destination of the teleportation effect (for example "the Plane of Fire," "north," or "Avistan"). On a critical success, you ascertain the exact destination within mere feet for local effects (such as *translocate*) or within a few miles for long-range effects (such as [[Teleport]], [[Interplanar Teleport]], or interdimensional portals).

**Activate—Triangulate** `pf2:1` (concentrate, manipulate)

**Frequency** once per day

**Effect** You use the compass of transpositional awareness to triangulate your current coordinates and those of your intended destination using teleportation magic. For 1 minute, whenever you cast a teleportation spell that has a range, increase that spell's range by 30 feet. If the spell normally has a range of touch, extend its range to 30 feet.

**Source:** `= this.source` (`= this.source-type`)
