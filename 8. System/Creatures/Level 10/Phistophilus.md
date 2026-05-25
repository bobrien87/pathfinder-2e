---
type: creature
group: ["Devil", "Fiend"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Phistophilus"
level: "10"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Devil"
trait_02: "Fiend"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+21; [[Greater Darkvision]]"
languages: "Aklo, Chthonian, Common, Diabolic, Draconic, Empyrean, Sakvroth (Telepathy 100 feet, Truespeech)"
skills:
  - name: Skills
    desc: "Arcana +19, Athletics +19, Deception +23, Diplomacy +21, Intimidation +21, Religion +19, Society +19, Stealth +18, Legal Lore +25"
abilityMods: ["+3", "+4", "+4", "+7", "+5", "+5"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Infernal Investment"
    desc: "A contract devil can cast a 10th-rank innate [[Scrying]] spell at will, but only to target a creature with which they have a contract. <br>  <br> The target automatically critically fails its save."
  - name: "Infernal Wound"
    desc: "The wounds from a contract devil's Strikes resist healing. <br>  <br> A spellcaster or item attempting to use healing magic on a creature suffering first attempts to counteract infernal wound (DC 29). If it is not counteracted, the healing has no effect."
armorclass:
  - name: AC
    desc: "30; **Fort** +18, **Ref** +18, **Will** +23"
health:
  - name: HP
    desc: "150; **Immunities** fire; **Weaknesses** holy 10; **Resistances** physical 10 except silver, poison 10"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Ward Contract"
    desc: "A signed contract carried by a living contract devil (including draped over its horns) is immune to damage from all creatures other than that contract devil. A contract devil is immune to mental effects that would make it destroy, nullify, or alter a contract."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Binding Contract +23 (`pf2:1`) (agile, disarm, magical, reach 10 ft., trip, unholy), **Damage** 3d6+11 slashing plus [[Grab]] plus [[Infernal Wound]]"
  - name: "Melee strike"
    desc: "Horn +21 (`pf2:1`) (magical, unarmed), **Damage** 3d10+11 piercing plus [[Infernal Wound]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 31, attack +23<br>**7th** [[Interplanar Teleport]]<br>**6th** [[Scrying (At Will, See Infernal Investment)]]<br>**5th** [[Illusory Scene]], [[Mind Probe]], [[Sending]] (At Will), [[Truespeech]] (Constant)<br>**4th** [[Peaceful Bubble]], [[Translocate]], [[Translocate]] (At Will)<br>**3rd** [[Fireball]], [[Lightning Bolt]], [[Locate]] (At Will), [[Mind Reading]] (At Will)<br>**2nd** [[Silence]]<br>**1st** [[Detect Magic]]"
abilities_bot:
  - name: "Draft Contract"
    desc: "`pf2:3` The contract devil produces an infernal contract for a single living mortal. This contract can grant a wide range of abilities and effects, akin to the power of a [[Wish]] ritual but fulfilled to the letter by the contract devil. To receive any of those benefits, the mortal must willingly sign its true name to the contract. At that point, the mortal's soul is bound to the contract devil and Hell. <br>  <br> While the contract is in effect, the victim can't be restored to life except by *wish* or similar magic. If the mortal is restored to life by those means, the contract devil knows which mortal came to life and can locate the creature or creatures who restored the mortal to life for 1 year, gaining the effects of a [[Locate]] spell with unlimited range. Avoiding the terms of an infernal contract is difficult and often dangerous."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Contract devils are clerks, scribes, and bureaucrats of Hell rarely found outside the infernal courts, and then almost always to pursue potential contracts, tempting mortals to sell their souls in exchange for achieving their worldly desires. If a target is desirable enough, a phistophilus can offer contracts for prices seemingly lesser than their soul all at once, though in this case, the devil carefully manipulates the price to drive the signatory toward the forces of Hell anyway. Contract devils are tall creatures with skin tones that range from bronze to crimson and large curving horns extending from their bodies, over which they often drape favored or important contracts.

Masters of corruption and architects of conquest, devils seek both to tempt mortal life to join in their pursuit of all things profane and to spread tyranny throughout all worlds. The temptations they offer mortals range from great powers granted by the signing of an infernal contract to twisted favors following a whispered pledge to a diabolic patron, or any number of even subtler exchanges. Those who succumb to these temptations find themselves consigned to an afterlife of endless torment in the pits of Hell, wherein the only hope of escape lies in the chance of being promoted to become a devil in the infernal ranks.

Every devil has a specific role to play in the upkeep of the remorseless bureaucratic machine that is Hell, from soldiers and scholars to inquisitors, lawyers, judges, and executioners. Lowly orts perform subservient labor to more powerful and specialized devils, such as infantry and contract devils, while the greatest nessaris command entire infernal armies.

Asmodeus stands at the apex of the structure he created, but the layers below him are marked by a constant jockeying for position. Most diabolic plans ultimately serve to improve the schemer's place in the hierarchy.

```statblock
creature: "Phistophilus"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
