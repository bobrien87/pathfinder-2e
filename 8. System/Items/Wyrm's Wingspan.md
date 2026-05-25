---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Invested]]", "[[Magical]]", "[[Tattoo]]"]
price: "{'gp': 700}"
usage: "tattooed-on-the-body"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A massive pattern resembling dragon wings stretched to their full span crosses your body. The tattoo is typically inked on the upper back. Though the representation can be highly stylized, each wyrm's wingspan tattoo depicts the wings of a particular type of dragon. You gain resistance 5 to the damage type matching the tradition of the dragon your tattoo depicts.

- **Arcane** force
- **Divine** spirit
- **Occult** mental
- **Primal** fire

**Activate** `pf2:2` (concentrate)

**Frequency** once per day

**Effect** The tattoo casts the [[Dragon Wings]] focus spell on you.

**Source:** `= this.source` (`= this.source-type`)
