---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Illusion]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 6500}"
usage: "worngarment"
bulk: "L"
source: "Pathfinder #211: The Secret of Deathstalk Tower"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This robe was the favored garment of the legendary Ekujae hero, Iyalirrin. When the draconic god Dahak threatened destruction, Iyalirrin was the primary architect of a powerful ritual to banish him called the anima invocation. Iyalirrin and many others were forced to sacrifice themselves to empower this ritual, but he ensured his *Anima Robe* remained in good hands before he did so. Since then, the *Anima Robe* has been worn by dozens of elven occultists and bards who have traveled Golarion and beyond. The *Anima Robe* has remained in the care of Queen Telandia for only the past few dozen years.

While wearing the *Anima Robe*, you gain a +2 item bonus to Diplomacy checks made to [[Make an Impression]] and to all Performance checks. You also gain resistance 10 to mental damage.

**Activate—Who Am I?** `pf2:1` (concentrate, illusion, manipulate, visual) With a toss of the robe's hood, you cast a 3rd-rank [[Illusory Disguise]] on yourself.

**Activate—Who Are We?** `pf2:1` (concentrate, illusion, manipulate, visual)

**Frequency** once per day

**Effect** With a whirl of the robe's hem, you cast a 7th-rank [[Illusory Disguise]].

**Activate—Who Are They?** `pf2:1` (auditory, concentrate, illusion, manipulate, olfactory, visual)

**Frequency** once per day

**Effect** With a swish of the robe's sleeve, you cast a 7th-rank [[Illusory Creature]].

**Source:** `= this.source` (`= this.source-type`)
