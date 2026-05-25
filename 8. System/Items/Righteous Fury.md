---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Holy]]", "[[Magical]]", "[[Versatile p]]"]
price: "{'gp': 6000}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This gold-plated *+2 greater striking holy longsword* sports an ornate hilt bearing the religious symbol of Ragathiel, General of Vengeance, and is painstakingly crafted to resemble the divine armaments wielded by the empyreal lord's celestial soldiers in their battles against the forces of darkness. These weapons are popular among the ranks of those who hold the line against similar enemies, such as the Knights of Lastwall and warriors of the former Mendevian Crusade.

**Activate—Great Vengeance** `pf2:1` (concentrate, divine, holy, spirit, vitality)

**Frequency** once per hour

**Trigger** Your last action was a successful melee Strike with righteous fury against a creature with the unholy trait

**Effect** The sword emits a 20-foot-radius emanation of holy fire centered on your target, inflicting @Damage[2d8[spirit],2d8[vitality]|options:area-damage]{2d8 spirit damage and 2d8 vitality damage} to all enemies in the area (DC 34 [[Reflex]] save). Creatures that fail the save are [[Blinded]] for 1 round, and those that critically fail are blinded for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
