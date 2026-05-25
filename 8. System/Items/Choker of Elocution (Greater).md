---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 850}"
usage: "worncollar"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This platinum choker bears characters from three language's alphabet, and it gives knowledge of those languages and the associated culture's customs.

You gain a +2 item bonus to Society checks and the ability to understand, speak, and write the chosen languages.

Your excellent elocution reduces the DC of the flat check to perform an auditory action while deafened from 5 to 3.

**Craft Requirements** You know the languages the choker grants.

**Source:** `= this.source` (`= this.source-type`)
