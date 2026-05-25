---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 2700}"
usage: "wornheadwear"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *greater submersible helmet* is a streamlined sallet with a visor and a flanged rear. While wearing the helmet with the visor down, you can see, hear, and speak clearly underwater. You also have a +2 item bonus to Athletics checks to Swim.

**Activate** `pf2:3` (concentrate, manipulate)

**Frequency** once per day

**Effect** You can breathe underwater for 8 hours. During this time, you have a swim Speed equal to your land Speed.

**Source:** `= this.source` (`= this.source-type`)
