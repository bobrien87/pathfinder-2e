---
type: creature
group: ["Fungus"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Myceloid"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Fungus"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10; [[Darkvision]], [[Scent]] (imprecise) 30 feet"
languages: "Sakvroth (Telepathy 100 feet (myceloids and those afflicted by purple pox only))"
skills:
  - name: Skills
    desc: "Stealth +11, Survival +10"
abilityMods: ["+4", "+3", "+4", "-1", "+2", "+0"]
abilities_top:
  - name: "Telepathy 100 feet (Myceloids and Those Afflicted by Purple Pox Only)"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Purple Pox"
    desc: "Myceloids are immune <br>  <br> **Saving Throw** DC 20 [[Fortitude]] save <br>  <br> **Onset** 1 minute <br>  <br> **Stage 1** 2d6 poison damage and [[Stupefied 1]] (1 day) <br>  <br> **Stage 2** 6d6 poison damage, [[Stupefied 3]], and the creature is compelled to seek out the nearest myceloid colony-this compulsion is a mental emotion effect (1 day) <br>  <br> **Stage 3** The creature dies. Over 24 hours, its corpse becomes bloated and bursts, releasing a new, fully grown myceloid."
armorclass:
  - name: AC
    desc: "20; **Fort** +14, **Ref** +9, **Will** +10"
health:
  - name: HP
    desc: "70; **Weaknesses** slashing 5"
abilities_mid:
  - name: "Spore Pop"
    desc: "If a myceloid is reduced to 0 HP by a critical hit, it pops, forcing it to immediately Emit Spores, even if it has already used the ability that day."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +14 (`pf2:1`) (unarmed), **Damage** 2d6+4 bludgeoning plus [[Purple Pox]]"
spellcasting: []
abilities_bot:
  - name: "Emit Spores"
    desc: "`pf2:1` **Frequency** once per day <br>  <br> **Effect** The myceloid expels spores in a @Template[burst|distance:10] centered on a corner of its own space. This cloud lasts until the start of the myceloid's next turn. Each creature that is in the cloud or enters it is exposed to purple pox."
  - name: "Spore Domination"
    desc: "`pf2:2` The myceloid targets one creature affected by purple pox within 60 feet. That creature must attempt a DC 22 [[Will]] save. <br>  <br> It is then temporarily immune to spore domination for 10 minutes. <br> - **Critical Success** The target is unaffected. <br> - **Success** Until the end of its next turn, the target is [[Helpful]] to myceloids and can't take hostile actions against them. <br> - **Failure** As success, but for 1 minute. <br> - **Critical Failure** As success, but until the purple pox is cured."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

The ambulatory fungus creatures called myceloids are notorious for spreading deadly purple pox, controlling creatures' minds, and devouring humanoid flesh. For a myceloid colony, any battle with humanoids is cause for excitement, as this new fodder presents so many delicious possibilities.

Myceloids consider humanoids to have an ideal life cycle of four simple steps. During childhood, they wander naive and afraid, unaware of myceloid colonies. In adulthood, humanoids discover their true purpose as they taste purple pox and become enslaved by the myceloids' spores. Next, they die, giving rise to a new myceloid. They're then sent on to the afterlife upon becoming a myceloid meal. Eating humanoid flesh is not a necessity-a myceloid can survive on any decaying matter-but it's certainly a pleasure.

Myceloids rarely make alliances, but when they do, they invite their new allies to share a meal to seal the pact. Few outsiders appreciate this hospitality.

Most myceloids have deep purple caps studded with off-white lumps. Their necks and bodies bear resemblance to the stipes of tough, leathery fungi. Smaller mushrooms often grow on a myceloid's body, which the creatures view as either adornments or particularly convenient snacks. They stand roughly as tall as a dwarf, with comparably stout builds.

```statblock
creature: "Myceloid"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
