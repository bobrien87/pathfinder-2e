---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Contract]]", "[[Invested]]", "[[Magical]]"]
price: "{'value': {}}"
usage: "other"
bulk: "—"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Sealed with a vial containing the ashes from your childhood home, you traded the memories of your early life to stay focused on the present, allowing you to avoid distractions during combat. Once per day, from any distance, the entity that holds your *bargained contract* can take one of your memories. This functions as a casting of [[Rewrite Memory]] that doesn't grant you a saving throw and can't be reversed by any means without stealing the memory back first.

**Activate—Fix Focus** `pf2:f` (concentrate)

**Frequency** once per day

**Trigger** You start your turn [[Off Guard]] or [[Confused]]

**Effect** A speck of ash from the vial sealing your *bargained contract* appears out of nowhere on your tongue, bringing your senses into focus. You suppress the [[Off Guard]] or [[Confused]] condition until the start of your next turn. You can use this free action when you're confused, even though you normally can't take actions of your choice when confused.

**Source:** `= this.source` (`= this.source-type`)
