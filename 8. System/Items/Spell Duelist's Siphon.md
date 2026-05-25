---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Grimoire]]", "[[Magical]]"]
price: "{'gp': 1750}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Metal clasps line the spine of this book, and diagrams displaying proper somatic casting forms are etched into its cover.

**Activate** R (concentrate)

**Frequency** once per day

**Trigger** You're targeted with an arcane spell attack and you have this grimoire raised

**Requirements** You have the [[Raise a Tome]] feat

**Effect** The grimoire attempts to absorb knowledge of the spell targeting you. You attempt to counteract the triggering spell. If you succeed, the spell is absorbed into the grimoire, and the diagrams on the cover change to indicate the somatic gestures and sigils for the counteracted spell. While the grimoire contains a spell, you can spend a spell slot of the same or higher rank as the spell in the grimoire to cast that spell instead, heightened to the appropriate rank (if you spent a higher-rank spell slot). After you cast the spell, it's expended from the grimoire.

**Source:** `= this.source` (`= this.source-type`)
