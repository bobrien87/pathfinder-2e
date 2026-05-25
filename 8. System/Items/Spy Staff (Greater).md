---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Illusion]]", "[[Magical]]", "[[Staff]]", "[[Two hand d8]]"]
price: "{'gp': 1175}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

In its normal form, a *spy staff* is a slim rod of burnished wood with subtle etchings of eyes upon its sides. The first to develop the spy staff were agents of Andoran's Twilight Talons, but such staves have spread to other espionage agencies.

**Activate** `pf2:1` (concentrate)

**Effect** You change the shape and appearance of this staff to that of an ordinary handheld accessory of your choosing of the same Bulk. The staff's statistics don't change. Only a creature benefiting from *truesight* or a similar effect can attempt to disbelieve this illusion, with a DC of 32.

**Activate** Cast a Spell

**Effect** You expend a number of charges from the staff to cast a spell from its list.

- **Cantrip** [[Message]]
- **1st** [[Illusory Disguise]], [[Invisible Item]], [[Message Rune]]
- **2nd** [[Disguise Magic]], [[Humanoid Form]], [[Illusory Disguise]]
- **3rd** [[Clairaudience]], [[Illusory Disguise]], [[Veil of Privacy]]
- **4th** [[Clairvoyance]], [[Peaceful Bubble]]

**Craft Requirements** Supply one casting of all listed ranks of all listed spells.

**Source:** `= this.source` (`= this.source-type`)
