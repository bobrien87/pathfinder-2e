---
type: creature
group: ["Aberration", "Earth"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Irlgaunt"
level: "13"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Aberration"
trait_02: "Earth"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+24; [[Darkvision]]"
languages: "Aklo, Common, Jotun, Petran"
skills:
  - name: Skills
    desc: "Acrobatics +25, Athletics +26, Deception +23, Stealth +27, Survival +22"
abilityMods: ["+7", "+8", "+5", "+4", "+5", "+4"]
abilities_top:
  - name: "At-Will Spells"
    desc: "The monster can cast its at-will spells any number of times without using up spell slots."
  - name: "Stone Step"
    desc: "The irlgaunt ignores difficult terrain composed of rocks and stone."
armorclass:
  - name: AC
    desc: "34; **Fort** +22, **Ref** +25, **Will** +24"
health:
  - name: HP
    desc: "265; **Immunities** acid; **Weaknesses** bludgeoning 10"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +26 (`pf2:1`), **Damage** 3d8+13 piercing plus 2d6 acid"
  - name: "Melee strike"
    desc: "Legs +26 (`pf2:1`) (agile), **Damage** 3d10+13 bludgeoning"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 31, attack +23<br>**5th** [[Speak with Stones]]<br>**4th** [[Shape Stone]] (At Will)<br>**3rd** [[One with Stone]] (At Will)"
abilities_bot:
  - name: "Regurgitate Gastrolith"
    desc: "`pf2:2` The irlgaunt violently regurgitates a melon-sized clot of brittle stone supernaturally infused with digestive enzymes. The stone and acid explode on impact within a range of 30 feet, dealing @Damage[7d6[piercing]|options:area-damage] damage and @Damage[7d6[acid]|options:area-damage] damage to creatures in a @Template[type:burst|distance:20] (DC 33 [[Reflex]] save). The irlgaunt can't Regurgitate Gastroliths for 1d4 rounds."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Irlgaunts resemble titanic spiders or crabs, but with cephalopod-like tendrils erupting from the tips of their chitin-armored legs. Their jagged gray shells allow them to blend into the rocky walls of the high mountain passes and deep ravines that serve as their hunting grounds. Despite their size, they move with incredible speed, bounding across chasms and skittering up sheer mountain cliffs in moments. Though they're formidable in melee, irlgaunts have an even more powerful ranged attack. These creatures pelt their opponents with forcefully regurgitated gastroliths—melon-sized clusters of rocks enveloped in coagulated digestive enzymes strong enough to break down flesh and bone. Gastroliths are fragile and explode on contact, spraying the area with shards of rock and caustic acid.

While one might easily mistake an irlgaunt for a simple, brutish beast, they have a keen intelligence and employ devious hunting strategies. They set traps for travelers and are fond of using gems and magical items taken from previous victims as bait. They've been known to start rockslides or otherwise block passages to reroute explorers into their clutches. They also use their gastroliths to direct the movements of their prey, forcing victims into dead ends at the edge of chasms or cliffs.

For the most part, irlgaunts live solitary lives, likely because finding enough food to sustain more than one tends to be difficult. However, they still maintain a sense of extended, regional community, actively gathering when organizing for war or to discuss other issues that affect their species or shared territories. They have been known to occasionally ally with giants, but these truces tend to be nebulous.

```statblock
creature: "Irlgaunt"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
