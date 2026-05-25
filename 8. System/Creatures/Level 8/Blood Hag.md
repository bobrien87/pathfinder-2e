---
type: creature
group: ["Hag", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Blood Hag"
level: "8"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Hag"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+17; [[Bloodsense]] (imprecise) 90 feet, [[Darkvision]]"
languages: "Aklo, Chthonian, Common, Diabolic, Jotun"
skills:
  - name: Skills
    desc: "Acrobatics +15, Athletics +18, Deception +19, Diplomacy +17, Occultism +16, Stealth +17"
abilityMods: ["+4", "+5", "+2", "+2", "+3", "+5"]
abilities_top:
  - name: "Bloodsense (Imprecise) 90 feet"
    desc: "A blood hag can sense the presence of blood and creatures with blood. They can tell the difference between spilled blood and the blood within a living creature."
  - name: "Borrowed Skin"
    desc: "A blood hag wears a covering of skin stolen from a humanoid creature they've killed, hiding their true form. They appear as the creature whose skin they're wearing, including to spells that would detect that creature. Creatures can still potentially detect the deception as described in the [[Impersonate]] action. <br>  <br> Spreading coarse salt inside the skin prevents the hag from putting it back on, forcing them to keep their fiery form until they kill another humanoid and spend 1 hour turning it into a new disguise."
  - name: "Coven"
    desc: "A blood hag adds [[Aerial Form]], [[Fiery Body]], and [[Nightmare]] to their coven's spells. <br>  <br> This monster can form a coven with two or more other creatures who also have the coven ability. This involves performing an 8-hour ceremony with all prospective coven members. After the coven is formed, each of its members gains elite adjustments, adjusting their levels accordingly. Coven members can sense other members' locations and conditions by spending a single action, which has the concentrate trait, and can sense what another coven member is sensing as a two-action activity, which has the concentrate trait as well. <br>  <br> Covens also grant spells and rituals to their members, but these can be cast only in cooperation between three coven members who are all within 30 feet of one another. A coven member can contribute to a coven spell with a single action that has the concentrate trait. If two coven members have contributed these actions within the last round, a third member can cast a coven spell on her turn by spending the normal spellcasting actions. A coven can cast its coven spells an unlimited number of times but can cast only one coven spell each round. All covens grant the 8th-rank [[Cursed Metamorphosis]] spell and all the following spells, which the coven can cast at any rank up to 5th: [[Augury]], [[Charm]], [[Clairaudience]], [[Clairvoyance]], [[Dream Message]], [[Illusory Disguise]], [[Illusory Scene]], [[Scouting Eye]], and [[Talking Corpse]]. Individual creatures with the coven ability also grant additional spells to any coven they join. A coven can also cast the [[Control Weather]] ritual, with a DC of 23 instead of the standard DC. <br>  <br> If a coven member's departure or death brings the coven below three members, the remaining members keep their elite adjustments for 24 hours, but without enough members to contribute the necessary actions, they can't cast coven spells."
armorclass:
  - name: AC
    desc: "26; **Fort** +14, **Ref** +17, **Will** +17"
health:
  - name: HP
    desc: "155; **Immunities** bleed; **Weaknesses** cold iron 10; **Resistances** fire 10"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +18 (`pf2:1`), **Damage** 2d12+7 piercing"
  - name: "Melee strike"
    desc: "Claw +18 (`pf2:1`) (agile), **Damage** 2d8+7 slashing plus [[Grab]]"
  - name: "Ranged strike"
    desc: "Firebolt +19 (`pf2:1`) (agile, fire, occult), **Damage** 5d6 fire"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 26, attack +18<br>**1st** [[Charm]], [[Sleep]]"
  - name: "Coven Spells"
    desc: "DC 26, attack +18<br>**7th** [[Fiery Body]]<br>**6th** [[Cursed Metamorphosis]]<br>**5th** [[Illusory Scene]], [[Scouting Eye]]<br>**4th** [[Aerial Form]], [[Clairvoyance]], [[Nightmare]], [[Talking Corpse]]<br>**3rd** [[Clairaudience]], [[Dream Message]]<br>**2nd** [[Augury]]<br>**1st** [[Charm]], [[Illusory Disguise]]"
abilities_bot:
  - name: "Assume Fiery Form"
    desc: "`pf2:3` The blood hag removes their borrowed skin and transforms into a brilliant ball of fire. They become amorphous (allowing them to move through a gap at least 1 foot wide without Squeezing and move at full Speed while Squeezing), gain the fire trait and a fly Speed of 60 feet, become immune to fire, and emit light as a torch. They lose their melee Strikes and can't Drain Blood, but they deal @Damage[4d6[fire]|options:area-damage] damage with a DC 26 [[Reflex]] save to each creature that touches them, including a creature that hits them with an unarmed attack or a weapon attack from an adjacent space. If their skin is intact and they're adjacent to it, they can Interact to return to their normal form inside the skin. <br>  <br> The hag can choose to Assume Fiery Form as a single action, bursting through their skin in a blast of flames. Doing so destroys their borrowed skin and deals @Damage[9d6[fire]|options:area-damage] damage to all creatures in a @Template[type:emanation|distance:20] with a DC 26 [[Reflex]] save. <br>  <br> > [!danger] Effect: Fiery Form"
  - name: "Drain Blood"
    desc: "`pf2:1` **Requirements** A [[Grabbed]], [[Paralyzed]], [[Restrained]], [[Unconscious]], or willing creature is within the blood hag's reach <br>  <br> **Effect** The hag sinks their fangs into the creature to drink its blood. This requires a successful Athletics check against the victim's Fortitude DC if the victim is grabbed and is automatic for any of the other conditions. The victim becomes [[Drained]] 1. The hag regains 15 Hit Points, gaining any excess HP as temporary Hit Points that last for 1 hour. Drinking blood from a creature that's already drained doesn't restore any Hit Points to the hag but increases the victim's drained value by 1, killing the victim when it reaches [[Drained]] 5. <br>  <br> A victim's drained condition decreases by 1 per week. A blood transfusion, which requires a successful DC 20 [[Medicine]] check and sufficient blood or a blood donor, reduces the drained condition by 1 after 10 minutes."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Blood hags, also known as soucouyants, infiltrate communities in the guise of young innocents. This disguise is more than an illusion, for a blood hag wears the skin of a previous victim to hide their true appearance. During the day, their disguise is almost perfect. But after sunset, the creature sheds their skin, hides it in a safe place, and stalks the night to drink the blood that sustains them.

Able to travel quickly in the form of a ball of fire and to slip through keyholes or the slightest crack in a door or window, blood hags feed on sleeping victims then return home before morning to don their stolen skin.

Hags are bizarre predators with uncertain origins, best known for targeting children and the young. To a one, they appear female, and they typically disguise themselves as mortal women in their day-to-day lives. Their powerful magic and manipulative tactics allow them to lure in the naive and vulnerable, exploiting their victims for their own sadistic purposes before kidnapping or devouring them. The typical hag is defined by a vain and controlling nature. Less malevolent hags may exist, but if so, they keep themselves well hidden to avoid the attentions of adventurers and their own abusive kin.

```statblock
creature: "Blood Hag"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
