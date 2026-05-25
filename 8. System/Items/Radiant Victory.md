---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Agile]]", "[[Finesse]]", "[[Magical]]", "[[Versatile s]]"]
price: "{'gp': 240}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This finely crafted *+1 striking shortsword* is carried by field marshals and other military officers who fight alongside their troops on the battlefield. Numerous other types of this blade exist, ranging from falchions to scimitars to longswords, and their appearances vary as widely as the nations and causes to which their wielders swear fealty. Many say that a soldier can tell the worth of their commanding officer by noting whether their primary weapon gives off the faint residual glow associated with a *radiant victory*.

**Activate—Rally the Troops** `pf2:1` (manipulate, visual)

**Frequency** once per day

**Requirements** You reduced a creature to 0 Hit Points with a Strike from the radiant victory as your last action

**Effect** You raise the blade high above your fallen enemy to inspire your comrades, projecting a blazing beacon into the sky that sheds bright light in a @Template[type:burst|distance:30] centered on you. This lasts for 1 minute and grants you and all allies within the area a +1 status bonus to attack rolls while within the light.

> [!danger] Effect: Rally the Troops

**Source:** `= this.source` (`= this.source-type`)
