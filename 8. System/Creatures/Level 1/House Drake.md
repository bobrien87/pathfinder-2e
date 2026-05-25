---
type: creature
group: ["Dragon"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "House Drake"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Tiny"
trait_01: "Dragon"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8; [[Darkvision]], [[Scent]] (imprecise) 30 feet"
languages: "Chthonian, Common, Daemonic, Diabolic, Draconic"
skills:
  - name: Skills
    desc: "Acrobatics +7, Society +4, Stealth +7, Survival +6"
abilityMods: ["+1", "+4", "+2", "+1", "+3", "+2"]
abilities_top:
  - name: "Silver Strike"
    desc: "House drakes sharpen their jaws on silver ornamentation until they incorporate bits of silver in their teeth. Their jaws Strike counts as silver."
armorclass:
  - name: AC
    desc: "17; **Fort** +6, **Ref** +8, **Will** +10"
health:
  - name: HP
    desc: "15; **Immunities** sleep, paralyzed"
abilities_mid:
  - name: "Ferocious Will"
    desc: "`pf2:r` **Trigger** The house drake succeeds at a saving throw against a magical mental effect <br>  <br> **Effect** The house drake sends a blast of magical feedback at the effect's source, dealing 2d6 mental damage (DC 16 [[Will]] save) to that creature. On a failed save, the creature is also [[Slowed]] 1 for 1 round."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +9 (`pf2:1`) (agile, finesse), **Damage** 1d8 + 1 piercing plus [[Silver Strike]]"
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 17, attack +9<br>**2nd** [[Mist]], [[See the Unseen]]<br>**1st** [[Alarm]], [[Soothe]]"
abilities_bot:
  - name: "Silver Breath"
    desc: "`pf2:2` The house drake breathes a @Template[type:cone|distance:10] of silver mist. Each creature within the mist must succeed at a DC 16 [[Will]] save or become [[Stupefied 2]] for 1 round. The house drake can't use Silver Breath again for 1d4 rounds."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Beautifully colored in purples and electric blues, the little dragonets called house drakes are genuinely brilliant in more ways than one. They're playful and kind, and while they have a long tradition of assisting spellcasters, they prefer to be treated as equals and partners rather than pets. They're quite intelligent and don't appreciate condescension from those who treat them as simple animals.

These tiny dragons have appeared in traditional Varisian tales for centuries, but only relatively recently have they become known by the name "house drake." This new name arose in the city of Korvosa, where house drakes have adapted particularly well to urban life. When students of the magic school called the Acadamae failed in their studies and allowed their imp familiars to run wild, these tiny dragons found that they were particularly well suited to combating them. The two species are well matched in cunning. Though their clashes typically begin with trying to outwit one another, they often end in messy brawls across rooftops and into alleys. The residents of Korvosa appreciated both the protection and the dragons' charming appearance and demeanor. As such, their population has flourished, and house drakes are more common in Korvosa than anywhere else in the world.

House drakes have peculiar grooming habits, often sharpening their teeth with silver coins or small jewelry. Because of this, their bites and exhalations are tinged with particles of silver. Otherwise, they're carnivorous, eating vermin and small birds. Though house drakes are capable of hunting for food, many of them find it a bit dull and will happily accept donations of food, preferring to spend their time at other pursuits. To truly get on a house drake's good side, though, one should offer a gift of silver. Donations to these dragonets have become regular practice in Korvosa, to the point where "paid any drakes lately?" has become a common phrase to suggest someone is a bit gullible and soft-hearted. These donations are just that—charity. House drakes avoid anything resembling a job, taking pride in their self-sufficiency and ability to choose how to spend their time.

```statblock
creature: "House Drake"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
