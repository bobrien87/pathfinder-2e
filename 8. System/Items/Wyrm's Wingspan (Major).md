---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Invested]]", "[[Magical]]", "[[Tattoo]]"]
price: "{'cp': 0, 'gp': 13500, 'pp': 0, 'sp': 0}"
usage: "tattooed-on-the-body"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A massive pattern resembling dragon wings stretched to their full span crosses your body. The tattoo is typically inked on the upper back. Though the representation can be highly stylized, each wyrm's wingspan tattoo depicts the wings of a particular type of dragon. You gain resistance 15 to the damage type matching the tradition of the dragon your tattoo depicts.

- **Arcane** force
- **Divine** spirit
- **Occult** mental
- **Primal** fire

**Activate** `pf2:2` (concentrate)

**Frequency** once per day

**Effect** The tattoo casts the [[Dragon Wings]] focus spell on you.

**Activate** `pf2:2` (concentrate)

**Frequency** once per day

**Effect** The tattoo casts an 8th-rank [[Dragon Form]] on you, turning you into the type of dragon represented by the tattoo.

**Source:** `= this.source` (`= this.source-type`)
