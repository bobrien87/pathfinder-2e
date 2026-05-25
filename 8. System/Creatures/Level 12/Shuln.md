---
type: creature
group: ["Beast"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Shuln"
level: "12"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Beast"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+20; [[Scent]] (imprecise) 30 feet, [[Tremorsense]] (imprecise) 60 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +25, Survival +22"
abilityMods: ["+7", "+4", "+6", "-3", "+4", "+1"]
abilities_top:
  - name: "Armor-Rending Strikes"
    desc: "Any time the shuln scores a critical hit with a melee Strike, it also deals the same amount of damage to the target's armor, bypassing any Hardness lower than 10, like adamantine."
  - name: "Shuln Saliva"
    desc: "**Saving Throw** DC 32 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 2d6 poison damage and [[Slowed]] 1 (1 round) <br>  <br> **Stage 2** 3d6 poison damage, and slowed 1 (1 round) <br>  <br> **Stage 3** 4d6 poison damage and [[Paralyzed]] for 2d6 hours. Shuln saliva overcomes the inexorable ability."
  - name: "Unstoppable Burrow"
    desc: "Shulns can burrow into solid rock and any metal with a hardness less than that of adamantine like it is soil or loose rubble, leaving a tunnel 10 feet in diameter."
armorclass:
  - name: AC
    desc: "33; **Fort** +25, **Ref** +19, **Will** +21"
health:
  - name: HP
    desc: "195; **Resistances** physical 10 except adamantine, bludgeoning, poison 15"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Adamantine Claw +25 (`pf2:1`) (adamantine, agile, reach 15 ft.), **Damage** 3d8+10 slashing"
  - name: "Melee strike"
    desc: "Adamantine Fangs +25 (`pf2:1`) (adamantine, reach 15 ft.), **Damage** 3d10+10 piercing plus [[Shuln Saliva]]"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Scourges of the upper Darklands, these enormous, mole-like monstrosities slice and burrow through solid stone with massive forearms and adamantine-strong claws. Shulns grow to about 20 feet long and have four tiny, nearly imperceptible eyes; a long, pale snout; four thick-muscled legs that end in long, serrated claws; and a stubby pink tail. As a young shuln matures, its unique metabolism produces adamantine that becomes infused throughout its skeletal system. In addition to making their claws and fangs nearly unbreakable, this unique physiological trait makes shulns unparalleled burrowers and highly sought by monster hunters who hope to harvest the precious material from their corpses.

Shulns have a ravenous appetite and eat nearly anything they can catch, but their preferred diet consists almost entirely of large invertebrates, especially cave worms. They rely on tiny sensory whiskers that cover their snouts and allow them to detect subtle movements in the air and ground without the use of vision. When they detect suitable prey, shulns bite their target at the first opportunity, injecting it with a potent paralytic toxin present in their saliva. So strong is this poison that it's capable of subduing even the near-unstoppable cave worm, making shulns a valuable (if dangerous) companion to anyone making excursions into worm-infested regions of the Darklands. Shulns' notoriously ill-tempered dispositions and their knack for digging into areas of an underground settlement where digging ought not to occur make them frustrating creatures to keep around, but when the alternative is an unpredictable but deadly visit from an enormous, hungry cave worm, the annoyances are well worth the trouble.

Encounters with much larger shuln-like entities on the Plane of Earth suggest that these creatures may have originated from there. The larger shulns still retain their elemental qualities, are quite a bit smarter, and have their own suite of earth-themed innate primal spells—but for all that, they still love the taste of cave worm.

```statblock
creature: "Shuln"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
