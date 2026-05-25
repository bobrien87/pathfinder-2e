---
type: creature
group: ["Shadow"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Shae"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Shadow"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10; [[Darkvision]]"
languages: "Aklo, Common, Sakvroth, Shae, Sussuran"
skills:
  - name: Skills
    desc: "Acrobatics +13, Deception +9, Occultism +11, Stealth +13, Netherworld Lore +11"
abilityMods: ["+3", "+5", "+1", "+3", "+2", "+3"]
abilities_top:
  - name: "Shadow Shift"
    desc: "Being made partially of shadow themselves, shae are [[Concealed]] in dim light or darkness even to creatures that can see clearly in those light levels."
  - name: "Swift Steps"
    desc: "The shae's movement doesn't trigger reactions."
  - name: "Tenebral Form"
    desc: "The shae can Fly at full Speed in [[Vapor Form]]."
armorclass:
  - name: AC
    desc: "21; **Fort** +9, **Ref** +11, **Will** +10"
health:
  - name: HP
    desc: "45; **Immunities** precision; **Resistances** cold 5, void 5"
abilities_mid:
  - name: "Counterattack"
    desc: "`pf2:r` **Trigger** The shae is targeted by an attack from an adjacent creature that misses due to the shae being [[Concealed]] <br>  <br> **Requirements** The shae is aware of the attack <br>  <br> **Effect** The shae makes a Strike against the attacker."
  - name: "Slip"
    desc: "`pf2:r` **Trigger** A creature moves adjacent to the shae <br>  <br> **Effect** The shae teleports to a clear space adjacent to another creature they can see within 30 feet."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +13 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+5 piercing plus 1d6 cold"
  - name: "Melee strike"
    desc: "Dagger +13 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4+5 piercing plus 1d6 cold"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 21, attack +13<br>**7th** [[Interplanar Teleport (self only; to Netherworld or Universe only)]]<br>**4th** [[Vapor Form]] (At Will)<br>**1st** [[Detect Magic]], [[Void Warp]]"
abilities_bot:
  - name: "Bide"
    desc: "`pf2:2` The shae prepares to take action against their foes, watching their opponent and waiting for the right opportunity to respond. The shae gains a second reaction until the start of their next turn, though they still can't use more than one reaction on the same triggering action."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Shae are wispy, tenebrous creatures native to the Plane of Shadow. Their amorphous bodies appear in constant states of flux. They cast no shadows of their own, instead gaining and losing umbral energy to nearby shadows that shrink and grow alongside them.

Most shae wear clothing spun from shadows that shift with them, though diplomats sometimes don more conventional garments while entertaining outsiders. Their most distinctive apparel are their white stone masks, which shae don only when they must put on a discernible "face" for interacting with humanoids and similar creatures. They do so begrudgingly, as they consider themselves superior to humanoids, but donning their masks allows them to be more easily understood and thus keeps their interactions with their lessers as brief as possible.

The dynamic between a shae and humanoids shifts when humanoids come to worship a shae, however. A mortal who shows a shae their due deference is worth keeping around, so many shae collect cults of personality or expansive entourages. Even getting a meeting with such a self-important shae can present a challenge that requires one to deal with many layers of hangers-on who insist on vetting the newcomer before wasting the shae's precious time.

According to shae lore, they've transcended the material world and now embody a cosmological equilibrium of reality and illusion. Their claims to metaphysical ascendance and knowledge of the secrets of shadows entice many mortal supplicants to join shae courts and cults. In the shae language, their name means "unbound," in accordance with their belief that their ephemeral nature makes them free of the moral and social strictures that bind other sentient creatures, and they essentially make a virtue of capriciousness. Shae feel little obligation to follow through with oaths or obey laws, so sealing a compact with a mortal means little to them.

```statblock
creature: "Shae"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
