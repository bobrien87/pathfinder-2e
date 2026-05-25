---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Invested]]", "[[Magical]]", "[[Teleportation]]"]
price: "{'gp': 210}"
usage: "wornmask"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

All *herd masks* are linked to at least one other herd mask and are usually sold in sets of multiple masks. Linked *herd masks* look like one another, with only slight differences to tell them apart.

**Activate** `pf2:1` (concentrate)

**Frequency** once per day

**Effect** You swap locations with another creature wearing a linked *herd mask* within 100 feet. If you and the creature you swapped with are disguised as each other, other creatures gain an immediate Perception check against the lower of your or the other wearer's Deception DCs to Impersonate each other. On a failure, they don't realize the swap occurred.

**Craft Requirements** Supply a casting of [[Translocate]]. You can link a *herd mask* you create to another *herd mask* in your possession when you finish crafting it, which causes it to be linked to the chosen mask as well as all other *herd masks* that are also linked to the chosen mask.

**Source:** `= this.source` (`= this.source-type`)
