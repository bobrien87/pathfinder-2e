---
type: creature
group: ["Plant", "Wood"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Arboreal Reaper"
level: "7"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Plant"
trait_02: "Wood"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+15; [[Low-Light Vision]]"
languages: "Arboreal, Common, Fey"
skills:
  - name: Skills
    desc: "Athletics +15, Intimidation +17, Nature +15, Stealth +14"
abilityMods: ["+6", "+2", "+4", "+2", "+2", "+4"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
armorclass:
  - name: AC
    desc: "25; **Fort** +17, **Ref** +13, **Will** +15"
health:
  - name: HP
    desc: "130; **Weaknesses** axe vulnerability 5, fire 10; **Resistances** bludgeoning 5, piercing 5"
abilities_mid:
  - name: "Axe Vulnerability"
    desc: "An arboreal reaper takes 5 additional damage from axes."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Branch +18 (`pf2:1`) (reach 10 ft.), **Damage** 2d10+8 bludgeoning"
  - name: "Melee strike"
    desc: "Root +18 (`pf2:1`) (agile), **Damage** 2d6+8 bludgeoning plus [[Knockdown]]"
  - name: "Ranged strike"
    desc: "Thorns +16 (`pf2:1`), **Damage** 2d8+5 piercing plus 1d4 bleed"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 22, attack +14<br>**3rd** [[Speak with Plants]] (Constant), [[Vampiric Feast]]"
abilities_bot:
  - name: "Leech Moisture"
    desc: "`pf2:2` The arboreal reaper grows still and focuses intently on a single foe within 50 feet, draining moisture from the target's body. This deals 10d6 void damage (DC 25 [[Fortitude]] save). <br>  <br> The arboreal reaper can't Leech Moisture again for 1d4 rounds."
  - name: "Knockdown"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Knockdown in its damage entry <br>  <br> **Effect** The monster attempts to `act trip` the creature. This attempt neither applies nor counts toward the monster's multiple attack penalty."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

While some forests have an idyllic, peaceful quality to them, others feel distinctly unfriendly or even sinister-these forests are the favored haunts of arboreal reapers. Sometimes these woodlands are sought out by secretive practitioners of malicious arts who claim the unsettling ambiance aids their abilities; arboreal reapers see no reason to interfere with such practices as long as the balance of their forests isn't harmed.

All arboreals vary in appearance based on their surroundings, but arboreal reapers always seem vaguely eerie, whether they watch over a grim weald or a tropical rain forest. Often slightly warped, twisted, and covered in spiky protrusions, arboreal reapers sometimes sprout around old ruins or other permanent structures, breaking down and incorporating the structures as they mature and become more mobile.

Arboreal reapers focus on the essential decaying phase of a forest's life cycle, becoming especially active in autumn and winter seasons. Their influence can often be seen in the explosion of mushrooms on a rotting log or the enticing fronds of a flourishing carnivorous plant. Like arboreal wardens, these woodland guardians are quicker to react to perceived threats than the more deliberate regents or retiring archives-at least by arboreal standards.

Arboreals are tree-like ancient guardians of forests, nurturing new growth and maintaining a balanced ecosystem as if the vast wilderness were their garden. Arboreals are thoughtful and deliberate - until something threatens their realms and invites their wrath.

```statblock
creature: "Arboreal Reaper"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
