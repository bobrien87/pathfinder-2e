---
type: creature
group: ["Devil", "Fiend"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Coarti"
level: "7"
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
    desc: "+17; [[Greater Darkvision]]"
languages: "Common, Diabolic, Draconic, Empyrean (Telepathy 100 feet, Truespeech)"
skills:
  - name: Skills
    desc: "Acrobatics +15, Athletics +15, Deception +17, Religion +17, Legal Lore +14"
abilityMods: ["+4", "+6", "+2", "+3", "+4", "+4"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
armorclass:
  - name: AC
    desc: "24; **Fort** +13, **Ref** +17, **Will** +15"
health:
  - name: HP
    desc: "110; **Immunities** fire; **Weaknesses** holy 5; **Resistances** physical 5 except silver, poison 5"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Blood Contract"
    desc: "When the coarti takes damage from their holy weakness, blood flows freely from their eyes and the contract carved into their skin. They take 1d6 persistent,bleed damage and are [[Dazzled]] as long as the persistent damage continues, but their Despairing Shriek recharges."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Morningstar +18 (`pf2:1`) (magical, unholy, versatile p), **Damage** 1d6+10 bludgeoning plus 1d6 spirit"
  - name: "Melee strike"
    desc: "Wing +17 (`pf2:1`) (agile, unholy, versatile p), **Damage** 1d6 fire plus 1d6+7 bludgeoning"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 25, attack +17<br>**5th** [[Truespeech]] (Constant)<br>**4th** [[Translocate]] (At Will)<br>**2nd** [[Darkness]]"
abilities_bot:
  - name: "Despairing Shriek"
    desc: "`pf2:2` The coarti lets out a terrible cry, dealing @Damage[4d6[sonic]|options:area-damage] damage to all creatures in a @Template[emanation|distance:30] with a DC 25 [[Will]] save. Holy creatures that fail this save are also [[Frightened]] 2; this added effect has the emotion, fear, and mental traits. <br>  <br> The coarti can't use Despairing Shriek again for 1d4 rounds."
  - name: "Wing Snap"
    desc: "`pf2:1` **Frequency** once per turn <br>  <br> **Effect** The coarti makes two wing Strikes, then falls if it's flying. It can't Fly until the end of its turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The burning-winged coartis are marked by the onerous contracts they agreed to and bound to Hell by the machinations of a legalistic devil, usually a phistophilus. Some coartis are truly a type of fallen celestial, those trapped in horrible agreements for the greater good or due to grievous errors in judgment, but most arise from mortal souls that were on the path to become celestials yet were contractually bound to Hell. Coartis serve in public roles as messengers and personal attendants to demonstrate the power of Hell and the legal acumen of their corruptors.

Celestials universally pity coartis and despise their creators, but their preferred methods of dealing with the corrupted beings differ. While angels argue against lost cases in Pharasma's courts, seeking loopholes in the voluminous contracts, azatas scheme daring heists against the contract storehouses. Archons are the most direct, working to end their blighted lives.

Masters of corruption and architects of conquest, devils seek both to tempt mortal life to join in their pursuit of all things profane and to spread tyranny throughout all worlds. The temptations they offer mortals range from great powers granted by the signing of an infernal contract to twisted favors following a whispered pledge to a diabolic patron, or any number of even subtler exchanges. Those who succumb to these temptations find themselves consigned to an afterlife of endless torment in the pits of Hell, wherein the only hope of escape lies in the chance of being promoted to become a devil in the infernal ranks.

Every devil has a specific role to play in the upkeep of the remorseless bureaucratic machine that is Hell, from soldiers and scholars to inquisitors, lawyers, judges, and executioners. Lowly orts perform subservient labor to more powerful and specialized devils, such as infantry and contract devils, while the greatest nessaris command entire infernal armies.

Asmodeus stands at the apex of the structure he created, but the layers below him are marked by a constant jockeying for position. Most diabolic plans ultimately serve to improve the schemer's place in the hierarchy.

```statblock
creature: "Coarti"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
