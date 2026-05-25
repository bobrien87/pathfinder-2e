---
type: creature
group: ["Humanoid", "Munavri"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Munavri Spellblade"
level: "2"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Humanoid"
trait_02: "Munavri"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+7; [[Darkvision]]"
languages: "Munavri, Sakvroth (Telepathy 30 feet (munavris only))"
skills:
  - name: Skills
    desc: "Athletics +8, Deception +7, Occultism +6, Stealth +4"
abilityMods: ["+4", "+0", "+2", "+0", "+1", "+3"]
abilities_top:
  - name: "Telepathy 30 feet (Munavris Only)"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Light Blindness"
    desc: "When first exposed to bright light, the monster is [[Blinded]] until the end of its next turn. After this exposure, light doesn't blind the monster again until after it spends 1 hour in darkness. However, as long as the monster is in an area of bright light, it's [[Dazzled]]."
armorclass:
  - name: AC
    desc: "18; **Fort** +8, **Ref** +6, **Will** +7"
health:
  - name: HP
    desc: "30; **Resistances** mental 2"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Bastard Sword +8 (`pf2:1`) (two hand d12), **Damage** 1d8+4 slashing"
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 17, attack +9<br>**1st** (3 slots) [[Daze]], [[Message]], [[Mindlink]], [[Phantom Pain]], [[Shield]], [[Soothe]], [[Telekinetic Projectile]]"
abilities_bot:
  - name: "Addling Strike"
    desc: "`pf2:1` **Frequency** once per turn <br>  <br> **Requirements** The munavri's most recent action was to Cast a Spell <br>  <br> **Effect** The munavri Strikes. This Strike gains the occult trait and deals an additional 1d4 mental damage."
  - name: "Intuit Object"
    desc: "`pf2:2` **Frequency** once per day <br>  <br> **Effect** By concentrating their psychic energy on a held object, the munavri intuits its use and understands how to effectively wield it. If they focus on a weapon, they can roll twice and take the better result for the next Strike they make with it before the end of their next turn. If they focus on a tool, they can roll twice and take the better result for the next skill check they attempt with that tool within the next minute."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Although the subterranean Darklands are known for the cruel and domineering civilizations led by fiend-worshipping peoples who dwell within those sinister caverns, not every such subterranean society is ruled that way. Munavris are perhaps the best example of a people who tend to treat new arrivals to their Darklands territories with good temper, fairness, and respect.

These humanoids are the descendants of humans who survived the world-ending cataclysm called Earthfall—mariners who were abducted by alghollthus and dragged down through the ocean depths until they emerged on the other side of the seafloor, amid the Sightless Sea in the lightless realm of Orv.

Gradually, munavris' bodies adapted to their new home: they began to demonstrate telekinetic powers and came to develop highly sensitive vision and beautiful crystalline growths along their skin, which is said to be a representation of their psychic abilities. These early munavris eventually settled on a mysterious archipelago of jade islands—mystical green landforms that seemed to resonate with strange and powerful psychic energies that repelled their alghollthu captors. Safe from their abductors and nurtured by the strange powers of their jade islands, munavris have remained free to hone their telekinetic abilities into substantial psychic prowess.

Every munavri has the ability to concentrate psychic energy upon an object and immediately ascertain what it is and how best to use it. Such amazing natural intuition doesn't come easily, however. Using this power requires munavris to expend a large portion of their limited psychic energy, and sleep is the only way for them to replenish this psychic well.

Today, nearly all munavris still dwell on the jade archipelago and ply the waters of the Sightless Sea. Their predominant culture promotes nobility of both deed and heart, and many munavris dedicate their lives to waging war against those who sow discord in the Darklands.

```statblock
creature: "Munavri Spellblade"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
