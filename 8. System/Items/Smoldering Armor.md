---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Fire]]", "[[Laminar]]"]
price: "{'gp': 975}"
bulk: "2"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+1 resilient fire-resistant niyaháat* is often created to mark the passage of an Erutaki warrior into adulthood, formed from plates salvaged from the exploded remains of a firewyrm elemental, with larger pieces protecting the chest, shoulders, and head. As you fight, the armor glows red hot.

**Activate** `pf2:2` (concentrate)

**Frequency** once per day

**Effect** The armor is sheathed in a [[Fire Shield]].

**Activate** `pf2:r` (concentrate)

**Frequency** once per day

**Trigger** You're dealt 30 or more fire damage, before any reduction from your fire resistance

**Requirements** You've used the *fire shield* activation already today

**Effect** The *fire shield* activation recharges.

**Craft Requirements** The initial raw materials must include the carapace of a firewyrm.

**Source:** `= this.source` (`= this.source-type`)
